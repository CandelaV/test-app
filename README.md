# test-app

Build image with kaniko and push to registry:

```
docker run -ti --rm -v `pwd`:/workspace -v `pwd`/config.json:/kaniko/.docker/config.json:ro gcr.io/kaniko-project/executor:latest --dockerfile=Dockerfile --destination=candelav/test-app:monitoring.v1
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

## Helm install

```
k create ns test-python-app
helm -n test-python-app upgrade --install test-app ./python-api-chart -f ./python-api-chart/values.yaml
```

```
k -n test-python-app port-forward $(kubectl get pod -n test-python-app | awk '/rest-api-/{print $1}') 8080:8000
```