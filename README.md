# test-app

Build image with kaniko and push to registry:

```
docker run -ti --rm -v `pwd`:/workspace -v `pwd`/config.json:/kaniko/.docker/config.json:ro gcr.io/kaniko-project/executor:latest --dockerfile=Dockerfile --destination=candelav/test-app:<tag>
```

Required `config.json` file in `pwd` with the following structure:

```
{
	"auths": {
		"https://index.docker.io/v1/": {
			"auth": "xxxxxxxxxxxxxxx"
		}
	}
}
```

Where `auth` is a string in `base64` composed of `USER:TOKEN`.