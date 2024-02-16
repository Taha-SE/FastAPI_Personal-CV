# Containerisierung des Projekts "FastAPI_Personal-CV"

In diesem Dokument werden die Schritte zur Containerisierung von einem FastAPI-Projekt. Dafür wird ein Docker-Image erstellt. Dieses Email wird dann auf verschiedenen Plattformen ausgeführt und getestet. 

## Inhaltverzeichnis 
- [Voraussetzungen](#voraussetzungen)
- [Docker Image erstellen](#docker-Image-erstellen)
- [Docker auf Windows](#docker-auf-Windows)
- [Docker auf Linux](#docker-auf-Linux)
- [Docker auf Gitlab CI/CD](#docker-auf-Gitlab-CI/CD-Pipeline)
- [Links](#links)


## Voraussetzungen
### Git-Repository clonen
Als erstes soll die Git-Repository von Github geclont werden.
Die Repo ist hier zu finden:
~~~
https://github.com/Taha-SE/FastAPI_Personal-CV.git
~~~

Anleitung hier => [Github-Anweisung](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette)

### Docker Desktop installieren
Docker Desktop ist eine Anwendung, die von Docker, Inc. entwickelt wurde und es ermöglicht, Docker-Container auf Desktop-Computern auszuführen.

Herunterladen => [Link](https://www.docker.com/products/docker-desktop/)

Installiere Docker Desktop und erstelle einen Konto auf [Docker-Hub](https://hub.docker.com/)

Eine Anleitung gibt es [Link](https://docs.docker.com/docker-id/)

## Docker-Image erstellen

Nach dem Clonen sollte die Projektstruktur wie folgt aus
~~~
/root:
    README.md
    requirements.txt
    [src]
        ├── crud.py
        ├── database.py
        ├── [db]
        ├── main.py
        ├── models.py
        ├── README.md
        ├── schemas.py
        ├── __init__.py
~~~

**Dockerfile erstellen**

Erstelle im Rootordner einen `Dockerfile` und füge folgenden Code hinzu

```
FROM python:3.9
WORKDIR /fastapi_cv_docker
COPY ./requirements.txt /fastapi_cv_docker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi_cv_docker/requirements.txt
COPY ./src /fastapi_cv_docker/src
EXPOSE 80
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
```

Der Dockerfile ist wie folgt zu erklären:

- `FROM python:3.9`: Diese Anweisung wählt das Basisimage für das Docker-Image aus. Hier wird das offizielle Python 3.9-Image als Ausgangspunkt verwendet.

- `WORKDIR /fastapi_cv_docker`: Mit dieser Anweisung wird das Arbeitsverzeichnis innerhalb des Containers auf /fastapi_cv_docker festgelegt. Alle nachfolgenden Befehle werden in diesem Verzeichnis ausgeführt.

- `COPY ./requirements.txt /fastapi_cv_docker/requirements.txt`: Hier wird die requirements.txt-Datei aus dem Hostsystem in das Arbeitsverzeichnis im Container kopiert. Diese Datei enthält die Python-Abhängigkeiten für die Anwendung.

- `RUN pip install --no-cache-dir --upgrade -r /fastapi_cv_docker/requirements.txt`: Diese Anweisung verwendet pip, um die Python-Abhängigkeiten aus der requirements.txt-Datei zu installieren. Das Flag --no-cache-dir verhindert die Verwendung von Zwischenspeichern, was die Größe des Docker-Images reduziert.

- `COPY ./src /fastapi_cv_docker/src`: Hier wird der Quellcode der FastAPI-Anwendung aus dem Hostsystem in das Arbeitsverzeichnis im Container kopiert.

- `EXPOSE 80`: Diese Anweisung öffnet den Port 80 im Container, damit die Anwendung darüber erreichbar ist. Beachten Sie, dass das Öffnen des Ports im Dockerfile nur eine deklarative Anweisung ist und nicht die tatsächliche Portfreigabe auf dem Host bewirkt.

- `CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]`: Dieser Befehl gibt die Standardbefehle an, die beim Start des Containers ausgeführt werden sollen. In diesem Fall wird die FastAPI-Anwendung mit Uvicorn gestartet und auf Port 80 im Container gehostet. Der Host wird auf "0.0.0.0" gesetzt, um die Anwendung von außerhalb des Containers erreichbar zu machen.

**Docker-Image erstellen**

~~~
docker build -t fastapi_cv_api:1.0 .
~~~

Dies erstellt ein Docker-Image mit dem Tag "fastapi_cv_api:1.0" basierend auf diesem Dockerfile im aktuellen Verzeichnis (.). "1.0" in dem Tag weist auf die Version hin.

# Docker auf Windows
Stell sicher, dass Docker Desktop im Hintergrund läuft

**Docker-Volume erstellen**
Ein Docker-Volume ist ein Mechanismus, der es ermöglicht, Daten zwischen dem Hostsystem und einem Docker-Container zu teilen oder dauerhaft zu speichern. Dies ist besonders nützlich, wenn Daten innerhalb eines Containers gespeichert werden müssen, die auch außerhalb des Containers zugänglich sein sollen.

~~~
docker volume create vdb-cv
~~~

**Docker-Image in einem Container ausführen**

Da das Image und Volume bereit sind, kann der Container ausgeführt werden. Dabei wird auf das Volume ist Hostsystem hingewiesen.
~~~
docker run -v /absoluter/pfad/zum/host/verzeichnis:/db fastapi-cv-api-image
~~~

Ersatzte `/absoluter/pfad/zum/host/verzeichnis` mit dem Pfad auf deinem Rechner

**Container öffnen**

Jezt soll es möglich sein auf dem Localhost:80 die CV-API zu benutzen und da ein Docker-Volume verwendet wird, werden die Daten weiterhin gespeichert, auch wenn das Container nicht mehr läuft.

Die Anwendung ist jetzt unter dem Localhost erreichbar. Zum Beispiel: "127.0.0.1" auf dem Port 80.

Docker Desktop bietet eine grafische Benutzeroberfläche, wodurch die Container gestartet, gestoppt und gelöscht werden können.

# Docker auf Linux

In diesem Dokument wird Manjaro Linux verwendet. 

## Docker auf Manjaro installieren

Bevor die Installation, stell dicher, dass das System auf dem neusten Stand ist.
~~~
$ sudo pacman -Syu
~~~

Danach kann Docker installiert werden

~~~
$ sudo pacman -S docker
~~~

Der nächste Schritt ist es, Docker zu aktivieren und zu starten

~~~
$ sudo systemctl start docker.service
$ sudo systemctl enable docker.service
~~~

Jetzt kann das Image von Docker-Hub gepullt werden. Das Image ist [hier](https://hub.docker.com/r/tahase/fastapi_cv-api) zu finden. Der tag 1.0 darf nicht fehlen.

~~~80
$ docker push tahase/fastapi_cv-api:1.0
~~~

Wie auf Windows muss zuerst ein Volume erstellt werden

~~~
$ docker volume create --opt type=none --opt device=/absoluter/pfad/auf/deinem/host/volume-name
~~~

Vergiss nicht den Pfad anzupassen.

Der letzte Schritt ist, das Image in einem Container auszuführen


~~~
$ docker run -v /absoluter/pfad/auf/deinem/host/volume-name:/db tahase/fastapi_cv-api:1.0
~~~

Für weitere Infos => [Manjaro Linux Docker installation](https://linuxconfig.org/manjaro-linux-docker-installation)

**Container öffnen**

Um der Localhost auf Manjaro Linux zu finden, kann der Befehl `ip addr` verwendet werden.

Jetzt kann die Anwendung einfach über den Localhost erreicht werden.

Hier ist ein Beispiel, wie es auf Manjaro läuft.
[CV-API Docker auf mein Manjaro Linux](https://drive.google.com/file/d/1wU5X-YNtu9lKFtVmnKd2ynX5J4kdpa6D/view?usp=sharing)

Auf dem Foto ist zu erkennen, dass der Container auf 172.17.0.2 läuft und dass das Volume damit verbunden ist.

# Docker auf Gitlab CI/CD

GitLab CI/CD (Continuous Integration/Continuous Deployment) ist eine integrierte Plattform in GitLab, die es Entwicklern ermöglicht, automatisierte Prozesse für die Integration, Bereitstellung und Testung von Softwareanwendungen zu erstellen. Die CI/CD-Pipeline ist eine automatisierte Arbeitsabfolge, die in mehrere Schritte unterteilt ist und auf jedem Commit (Änderung im Code) in einem GitLab-Repository automatisch ausgelöst wird.

## Gitlab CI/CD Pipeline für Docker erstellen

**GitLab-Repository erstellen**

Der erste Schritt besteht daran, ein GitLab-Repository zu erstellen und das Projekt mit dem Dockerfile darauf zu push. Die Anleitung dafür ist [hier]("https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-add-and-push-an-existing-project-to-GitLab")

**Gitlab Runner**

Der Runner führt die CI/CD-Jobs in der Pipline aus. Wie ein Runner installiert und ausgeführt werden kann, ist [hier]("https://docs.gitlab.com/ee/tutorials/create_register_first_runner/") erklärt.

**.gitlab-ci.yml erstellen**

Um die CI/CD-Pipeline für das Projekt zu definieren und zu steuern, wird eine Gitlab-Konfigurationsdatei `.gitlab-ci.yml` benötigt. 

Erstelle ein `.gitlab-ci.yml` mit folgender Struktur:

~~~
image: docker:latest
stages:
  - build
variables:
  IMAGE_NAME: cv-api
services: 
  - docker:dind
build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY/tahase1/cv-api-docker/$IMAGE_NAME .
    - docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
    - docker push $CI_REGISTRY/tahase1/cv-api-docker/$IMAGE_NAME
~~~

- `image: docker:latest` : Verwendet das Docker-Image "latest" als Basisimage für den GitLab Runner.
- `stages: - build` : Definiert die Phasen (Stages) für die Pipeline und legt die erste Phase mit dem Namen "build" fest.
- `variables: ` : Definiert Umgebungsvariablen für die Pipeline.
- `IMAGE_NAME: cv-api` : Weist der Umgebungsvariable "IMAGE_NAME" den Wert "cv-api" zu.
- `services: ` : Legt die Docker-Dienste fest, die während der Pipeline verwendet werden.
- `- docker:dind ` : Startet den Docker-in-Docker (dind)-Dienst, der Docker-Operationen in der Pipeline ermöglicht.
- `build: ` : Definiert einen Job mit dem Namen "build" in der Phase "build".
- `stage: build ` : Weist dem Job die Phase "build" zu.
- `script: ` : Definiert die Befehle, die im Job ausgeführt werden sollen.
- `- docker build -t $CI_REGISTRY/tahase1/cv-api-docker/$IMAGE_NAME . ` : Erstellt ein Docker-Image und gibt ihm einen Namen unter Verwendung von Umgebungsvariablen und dem aktuellen Verzeichnis als Build-Kontext.
- `- docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD ` : Authentifiziert sich beim Docker-Registry mit den GitLab-Registrierungsdaten.
- `- docker push $CI_REGISTRY/tahase1/cv-api-docker/$IMAGE_NAME ` : Lädt das erstellte Docker-Image in den Docker-Registry hoch, der in den GitLab-Registrierungsdaten angegeben ist.

**CI/CD Pipeline ausführen**

Commite und Pushe die Änderungen in das GitLab-Repository. Dies löst automatisch die CI/CD-Pipeline aus, die in der .gitlab-ci.yml-Datei definiert ist.

# Links

**Link zum orginalen Github-Repository**

https://github.com/Taha-SE/FastAPI_Personal-CV

**Link zum Image auf Docker-Hub**

https://hub.docker.com/r/tahase/fastapi_cv-api

**Link zum Gitlab-Repository**

https://gitlab.com/tahase1/cv-api-docker


---
**Danke!**
