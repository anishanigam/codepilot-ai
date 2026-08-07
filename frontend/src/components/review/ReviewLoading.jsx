import {
  Brain,
  Shield,
  Bug,
  FileText,
  Sparkles,
  CheckCircle2,
} from "lucide-react";
import { useEffect, useState } from "react";

function ReviewLoading() {
  const [currentStep, setCurrentStep] = useState(0);

  const steps = [
    {
      icon: <Brain size={22} />,
      text: "Planning AI Review",
    },
    {
      icon: <Bug size={22} />,
      text: "Running Bug Detection Agent",
    },
    {
      icon: <Shield size={22} />,
      text: "Running Security Agent",
    },
    {
      icon: <Sparkles size={22} />,
      text: "Running Best Practices Agent",
    },
    {
      icon: <FileText size={22} />,
      text: "Generating Executive Summary",
    },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStep((prev) =>
        prev < steps.length - 1
          ? prev + 1
          : prev
      );
    }, 1200);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="mx-auto flex min-h-[70vh] max-w-3xl items-center justify-center px-6">

      <div className="w-full rounded-3xl border bg-white p-10 shadow-lg">

        <div className="text-center">

          <Brain
            size={55}
            className="mx-auto text-blue-600"
          />

          <h1 className="mt-6 text-4xl font-bold">
            AI Review in Progress
          </h1>

          <p className="mt-3 text-gray-500">
            CodePilot AI is reviewing your pull request using multiple specialized agents.
          </p>

        </div>

        <div className="mt-10 space-y-5">

          {steps.map((step, index) => (

            <div
              key={step.text}
              className={`flex items-center gap-4 rounded-xl border p-4 transition-all

              ${
                index <= currentStep
                  ? "bg-green-50 border-green-200"
                  : "bg-gray-50"
              }
              `}
            >

              {index < currentStep ? (

                <CheckCircle2
                  className="text-green-600"
                />

              ) : (

                step.icon

              )}

              <span className="font-medium">

                {step.text}

              </span>

            </div>

          ))}

        </div>

        <p className="mt-8 text-center text-sm text-gray-500">

          This usually takes around 10–20 seconds.

        </p>

      </div>

    </div>
  );
}

export default ReviewLoading;