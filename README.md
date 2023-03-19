# xlwings Server with DigitalOcean Functions

DigitalOcean functions need to be deployed using `doctl`, the DigitalOcean CLI:

* Install doctl: https://docs.digitalocean.com/reference/doctl/how-to/install/
* In the DigitalOcean dashboard, under Functions: Create a namespace, e.g., `xlwings`

In a local Terminal/Command Prompt:
* `doctl serverless install`
* `doctl serverless connect <your-namespace>`
* Clone or download this repository
* Change into this repository's root directory: `cd xlwings-server-digitaloceanfunctions`
* In the root directory, create an `.env` file and fill in your xlwings license key: `cp .env.template .env`
* Make `build.sh` executable on macOS/Linux: `chmod +x packages/mypackage/hello/build.sh`
* Deploy: `doctl serverless deploy . --remote-build`


In the DigitalOcean Dashboard, find your function and copy its URL. Use this URL in your `RunRemotePython` (VBA) or `runPython` (JavaScript) call, respectively. Alternatively, you can also get the URL by running `doctl sls fn get mypackage/hello --url` in the Terminal/Command Prompt.

Make sure that the xlwings module on the client side (i.e., the VBA or JavaScript module) has the same version as in `requirements.txt`.