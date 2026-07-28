from pathlib import Path
import re

from app.ai.constants import (
    SUPPORTED_EXTENSIONS,
    IGNORED_DIRECTORIES,
    IGNORED_FILENAMES,
    MAX_PATCH_LINES,
    CHUNK_OVERLAP,
    BOUNDARY_SEARCH_WINDOW
)
from app.ai.models import (
    GitHubFile,
    ReviewableFile,
    SkippedFile,
    ReviewStatistics,
    PreprocessorResult,
)


class ReviewPreprocessor:

    BOUNDARY_PATTERNS = {
    "python": (
        "def ",
        "async def ",
        "class ",
    ),

    "javascript": (
        "function ",
        "class ",
        "const ",
        "let ",
        "var ",
        "export ",
    ),

    "typescript": (
        "function ",
        "class ",
        "const ",
        "let ",
        "export ",
        "interface ",
    ),

    "java": (
        "public class",
        "class ",
        "interface ",
        "enum ",
        "public ",
        "private ",
        "protected ",
    ),

    "cpp": (
        "class ",
        "struct ",
        "template",
        "namespace",
    ),

    "go": (
        "func ",
        "type ",
    ),
}

    def is_supported_file(self, filename: str) -> bool:
        extension = Path(filename).suffix.lower()
        return extension in SUPPORTED_EXTENSIONS

    def detect_language(self, filename: str) -> str:
        extension = Path(filename).suffix.lower()
        return SUPPORTED_EXTENSIONS[extension]

    def is_generated_file(self, filename: str) -> bool:
        path = Path(filename)

        if path.name in IGNORED_FILENAMES:
            return True

        return any(
            directory in path.parts
            for directory in IGNORED_DIRECTORIES
        )

    def normalize_patch(self, patch: str) -> str:
        return (
            patch.replace("\r\n", "\n")
            .replace("\r", "\n")
            .strip()
        )

    def split_into_hunks(self, patch: str) -> list[str]:
        """
        Split a git patch into logical hunks.

        Every hunk starts with a line like:

        @@ -10,5 +10,7 @@

        Returns a list of complete hunks.
        """

        hunk_header_pattern = r"(?=^@@.*@@)"

        hunks = re.split(
            hunk_header_pattern,
            patch,
            flags=re.MULTILINE,
        )

        return [
        hunk.strip()
        for hunk in hunks
        if hunk.strip()
        ]


    def find_best_split(
        self,
        lines: list[str],
        start: int,
        end: int,
        language: str,
    ) -> int:
        """
        Find the best location to split a large git hunk.
        
        The search prefers semantic boundaries such as
        functions, classes, and language-specific declarations
        over blank lines.
        
        Searching is limited to a small window near the
        target split point so chunk sizes remain balanced.
        
        Priority:
            1. Function / method declarations
            2. Class declarations
            3. Language-specific declarations
            4. Blank lines
            5. Hard split
        """

        patterns = self.BOUNDARY_PATTERNS.get(language.lower(), ())

        search_start = max(start, end - BOUNDARY_SEARCH_WINDOW)


    # Pass 1 : semantic boundaries
        for i in range(end - 1, search_start - 1, -1):

            stripped = lines[i].lstrip()

            if any(
            stripped.startswith(pattern)
            for pattern in patterns
            ):
                return i

    # Pass 2 : blank lines
        for i in range(end - 1, search_start - 1, -1):

            if lines[i].strip() == "":
                return i

    # Pass 3 : hard split
        return end


    def split_large_hunk(
    self,
    hunk: str,
    language: str,
) -> list[str]:

        lines = hunk.splitlines()

        if len(lines) <= MAX_PATCH_LINES:
            return [hunk.strip()]

        chunks = []

        start = 0

        OVERLAP = CHUNK_OVERLAP

        while start < len(lines):

            end = min(
                start + MAX_PATCH_LINES,
                len(lines),
            )

            if end == len(lines):

                chunks.append(
                    "\n".join(lines[start:end]).strip()
                )

                break

            split_index = self.find_best_split(
                lines,
                start,
                end,
                language,
            )

            if split_index <= start:
                split_index = end

            chunk = "\n".join(
                lines[start:split_index]
            ).strip()

            chunks.append(chunk)

            next_start = split_index - OVERLAP

            if next_start <= start:
                start = split_index
            else:
                start = next_start

        return chunks

    def chunk_patch(
        self,
        patch: str,
        language: str,
    ) -> list[str]:
            """
            Convert a git patch into AI-ready chunks.
        
            Workflow:
                Patch
                    ↓
                Hunks
                    ↓
                Large Hunk Splitter
                    ↓
                Final Chunks
            """
    
            patch = self.normalize_patch(patch)
        
            hunks = self.split_into_hunks(patch)
        
            chunks = []
        
            for hunk in hunks:
            
                chunks.extend(
                    self.split_large_hunk(
                        hunk,
                        language,
                    )
                )
        
            return chunks
    

    def process(
        self,
        files: list[GitHubFile],
    ) -> PreprocessorResult:

        reviewable: list[ReviewableFile] = []
        skipped: list[SkippedFile] = []

        for file in files:

            # Unsupported file extension
            if not self.is_supported_file(file.filename):
                skipped.append(
                    SkippedFile(
                        filename=file.filename,
                        reason="unsupported_extension",
                        details=Path(file.filename).suffix.lower(),
                    )
                )
                continue

            # Generated file
            if self.is_generated_file(file.filename):
                skipped.append(
                    SkippedFile(
                        filename=file.filename,
                        reason="generated_file",
                    )
                )
                continue

            # Binary / No textual diff
            if not file.patch:
                skipped.append(
                    SkippedFile(
                        filename=file.filename,
                        reason="non_text_file",
                    )
                )
                continue

            language = self.detect_language(file.filename)

            reviewable.append(
                ReviewableFile(
                    filename=file.filename,
                    language=language,
                    status=file.status,
                    additions=file.additions,
                    deletions=file.deletions,
                    changes=file.changes,
                    chunks=self.chunk_patch(
                        file.patch,
                        language,
                    ),
                )
            )

        return PreprocessorResult(
            reviewable_files=reviewable,
            skipped_files=skipped,
            statistics=ReviewStatistics(
                total_files=len(files),
                reviewable_files=len(reviewable),
                skipped_files=len(skipped),
            ),
        ) 

preprocessor = ReviewPreprocessor()