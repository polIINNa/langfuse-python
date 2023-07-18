# Langfuse Javascript SDK

[![npm package](https://img.shields.io/npm/v/langfuse?style=flat-square)](https://www.npmjs.com/package/langfuse)
[![MIT License](https://img.shields.io/badge/License-MIT-red.svg?style=flat-square)](https://opensource.org/licenses/MIT)

```
pip install langfuse
```

Full documentation: https://docs.langfuse.com/sdk/python


## Development

### Update openapi spec
1. Generate Fern Python SDK in [langfuse](https://github.com/langfuse/langfuse) and copy the files generated in `generated/python` into the `langfuse/api` folder in this repo.
2. Rebuild and deploy the package to PyPi.

### Deployment
1. poetry version patch
2. poetry build
3. poetry publish