# 📘 Documentation & Cahier de charges

## 1. Présentation générale

### 1.1 Contexte

Dans de nombreux environnements urbains et semi‑urbains, les citoyens sont souvent les premiers témoins d’incidents : accidents, vols, inondations, incendies, troubles sécuritaires, etc. L’absence d’un canal numérique rapide et géolocalisé limite la diffusion d’informations utiles à la population.

Ce projet vise à créer une **application d’alerte d’urgence géolocalisée**, permettant aux **citoyens** et aux **autorités** de signaler des situations à risque et d’informer immédiatement les personnes concernées selon leur position géographique.

---

### 1.2 Objectif du projet

Mettre en place une plateforme fiable permettant :

* La **création d’alertes citoyennes locales**
* La **diffusion instantanée d’alertes** aux utilisateurs proches
* La **gestion des fausses alertes** par signalement
* La **différenciation claire** entre alertes citoyennes et officielles

---

## 2. Objectifs spécifiques

* Fournir une information rapide en cas de danger
* Réduire les fausses alertes par un mécanisme communautaire simple
* Exploiter la géolocalisation pour limiter les alertes aux zones concernées
* Proposer une base évolutive vers un système plus avancé (votes, fiabilité, autorités)

---

## 3. Périmètre du projet (V1)

### Inclus

* Création d’alertes par les citoyens
* Création d’alertes officielles par les autorités
* Géolocalisation des utilisateurs
* Notifications push
* Signalement de fausse alerte
* Suppression automatique d’alertes abusives

### Exclus (V1)

* Vote de confirmation positive
* Score de confiance utilisateur
* Intelligence artificielle
* Mode hors‑ligne

---

## 4. Types d’alertes

### 4.1 Alertes citoyennes

* Vol / braquage
* Accident routier
* Inondation locale
* Incendie domestique
* Danger ponctuel

**Caractéristiques** :

* Non officielles
* Diffusion immédiate
* Supprimables par signalements

### 4.2 Alertes officielles

* Catastrophes majeures
* Alertes sécuritaires
* Alertes sanitaires

**Caractéristiques** :

* Émises par autorités
* Marquées comme OFFICIELLES
* Non supprimables automatiquement

---

## 5. Acteurs du système

| Acteur         | Description                           |
| -------------- | ------------------------------------- |
| Citoyen        | Utilisateur standard de l’application |
| Autorité       | Institution officielle habilitée      |
| Administrateur | Gestion technique de la plateforme    |

---

## 6. Fonctionnalités principales

### 6.1 Gestion des utilisateurs

* Inscription / connexion
* Autorisation de géolocalisation
* Attribution de rôles

### 6.2 Gestion des alertes

* Création d’alerte (citoyen / autorité)
* Définition de la position et du rayon
* Statuts d’alerte : active, limitée, supprimée

### 6.3 Signalement de fausse alerte

* Bouton « Signaler comme fausse »
* Un signalement par utilisateur
* Seuils de réduction / suppression

---

## 7. Cycle de vie d’une alerte citoyenne

1. Création par un citoyen
2. Diffusion immédiate
3. Réception par les utilisateurs proches
4. Signalements possibles
5. Réduction ou suppression automatique

---

## 8. Règles de gestion (Business Rules)

* Une alerte est **ACTIVE** par défaut
* À partir de X signalements → **LIMITÉE**
* À partir de Y signalements → **SUPPRIMÉE**
* Une alerte supprimée disparaît pour tous
* Les alertes officielles ignorent ces règles

---

## 9. Exigences non fonctionnelles

### 9.1 Performance

* Notification < 5 secondes
* Réponse API < 300 ms

### 9.2 Sécurité

* Authentification JWT
* Chiffrement HTTPS
* Protection contre abus

### 9.3 Confidentialité

* Consentement explicite GPS
* Pas de partage public des positions
* Données conformes RGPD‑like

---

## 10. Architecture technique (prévisionnelle)

* Backend : FastAPI (Python)
* Base de données : PostgreSQL + PostGIS
* Mobile : Flutter ou React Native
* Notifications : Firebase Cloud Messaging
* Cartographie : OpenStreetMap / Google Maps

---

## 11. Contraintes

* Connexion Internet parfois instable
* Utilisation mobile prioritaire
* Scalabilité progressive

---

## 12. Évolutions futures

* Vote de confirmation
* Score de fiabilité utilisateur
* Notifications SMS
* Tableau de bord autorités
* IA de détection d’anomalies

---

## 13. Critères de réussite

* Les alertes sont reçues rapidement
* Les fausses alertes sont maîtrisées
* L’application est simple à utiliser
* Les utilisateurs font confiance au système

---

📌 **Ce document sert de base officielle pour le développement du projet.**
