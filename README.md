# sample-functions-lambda

Part of the ForeCode test estate. Not a real product.

Python functions deployed to AWS Lambda with the AWS SAM CLI: to `staging` on every change to `main` and on a
schedule, and to `production` when run manually (the `production` environment needs an approval). Both stages use one
reusable deploy job, called twice.

Deploys are simulated: `.github/simulate.sh` makes the deploy tools print what they would do.
