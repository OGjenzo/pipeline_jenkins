# Pipeline_jenkins : Apprentissage des Pipelines et de la Logique CI/CD avec Jenkins

**Description :**

Notre projet d'apprentissage vise à explorer en profondeur les concepts des pipelines et de la logique CI/CD en utilisant l'outil Jenkins. Nous allons suivre un scénario de pipeline spécifique pour comprendre chaque étape du processus, du clonage du projet à partir du référentiel GitHub à son déploiement réussi sur un serveur de production à l'aide de Docker Compose.

**Scénario du Pipeline :**

**Clonage du Projet :** Le processus démarre par le clonage du code source à partir du référentiel GitHub. Cette étape est cruciale car elle assure que le pipeline travaille avec la version la plus récente du code.

**Build de l'Application :** Après avoir cloné le projet, l'application est construite à l'aide des outils appropriés. Le build garantit que le code source est compilé correctement et que l'application est prête pour les tests.

**Test de l'Application :** Une fois l'application construite, elle est soumise à des tests pour garantir son bon fonctionnement. Les tests peuvent inclure des tests unitaires, des tests d'intégration et des tests de système pour vérifier chaque composant de l'application.

**Push de l'Image dans Docker Hub :** Après avoir réussi les tests, l'image de l'application est construite et poussée dans Docker Hub **kbenalaya/cocadminapp**. Cela crée une version encapsulée et prête à être déployée sur n'importe quel serveur compatible avec Docker .

**Déploiement sur le Serveur de Production ou dans un Environnement Kubernetes :** L'image de l'application, disponible dans Docker Hub, peut être déployée soit sur un serveur de production traditionnel, soit dans un cluster Kubernetes en fonction des exigences spécifiques du projet. Dans le contexte d'un serveur de production, l'application est récupérée à partir de Docker Hub et déployée de manière fiable en utilisant Docker Compose à l'aide de la commande docker-compose up. Cela garantit une cohérence dans le déploiement de l'application sur le serveur de production. 

**avant un build**

![image](https://github.com/OGjenzo/pipeline_jenkins/assets/125826820/7090c875-18b7-4743-9d83-9311cce8b2ee)

**aprés un build ( changement de l'image docker et remise a zero du compteur redis)**

![image](https://github.com/OGjenzo/pipeline_jenkins/assets/125826820/72e5a72a-323e-4026-ac10-ce874ea3b390)

