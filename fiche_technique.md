# 🧾 FICHE TECHNIQUE DU PROJET

## Nom du projet

**Plateforme d’alerte d’urgence géolocalisée (citoyens & autorités)**

---

## 1. Description générale

Application multi-plateforme permettant la **création, diffusion et gestion d’alertes d’urgence géolocalisées**. Les alertes peuvent être émises par les citoyens (incidents locaux) ou par les autorités (urgences officielles), et sont transmises automatiquement aux utilisateurs situés dans la zone concernée.

---

## 2. Objectifs techniques

* Diffusion rapide d’informations critiques
* Géolocalisation précise des alertes
* Notifications temps réel
* Gestion simple des fausses alertes
* Architecture scalable et évolutive

---

## 3. Architecture globale

### Type d’architecture

* **Client – API – Services**
* Architecture modulaire orientée services

### Composants principaux

* Backend API centralisé
* Frontend Web Administrateur
* Frontend Web Utilisateur
* Application mobile cross-platform

---

## 4. Backend (API centrale)

### Rôle

* Logique métier
* Gestion des utilisateurs et rôles
* Gestion des alertes
* Géolocalisation
* Notifications push

### Technologies

* **Langage** : Python 3.11+
* **Framework** : FastAPI
* **Base de données** : PostgreSQL
* **Extension géographique** : PostGIS
* **ORM** : SQLAlchemy
* **Notifications** : Firebase Cloud Messaging (FCM)
* **Cache / rate limit** (optionnel) : Redis
* **Reverse proxy** : Nginx

### Sécurité

* Authentification JWT
* HTTPS
* Rôles (citoyen, autorité, admin)
* Limitation de requêtes

### Modules principaux

* Authentification
* Utilisateurs
* Alertes
* Signalements de fausses alertes
* Notifications
* Géolocalisation

---

## 5. Frontend Web Administrateur

### Rôle

* Supervision du système
* Création d’alertes officielles
* Gestion et modération des alertes
* Visualisation globale

### Technologies

* React.js ou Next.js
* TypeScript
* Tailwind CSS / Material UI
* Axios
* Leaflet ou Google Maps

### Fonctionnalités

* Authentification sécurisée
* Tableau de bord statistiques
* Carte globale des alertes
* Gestion des utilisateurs
* Suppression manuelle d’alertes

---

## 6. Frontend Web Utilisateur (citoyen)

### Rôle

* Consulter les alertes
* Créer une alerte citoyenne
* Signaler une fausse alerte
* Visualiser les zones à risque

### Technologies

* React.js ou Vue.js
* PWA (Progressive Web App)
* Leaflet + OpenStreetMap
* API Geolocation navigateur

### Fonctionnalités

* Géolocalisation automatique
* Carte interactive
* Notifications web
* Historique des alertes

---

## 7. Application Mobile (Cross-Platform)

### Rôle

* Canal principal de réception d’alertes
* Utilisation en mobilité

### Technologies recommandées

* **Flutter** (Android & iOS)
* Firebase (FCM)
* GPS natif

### Fonctionnalités

* Authentification
* Réception de notifications push
* Création rapide d’alertes
* Carte temps réel
* Signalement de fausses alertes

---

## 8. Gestion des alertes

### Types d’alertes

* **Citoyennes** : incidents locaux
* **Officielles** : urgences institutionnelles

### Cycle de vie (citoyen)

* ACTIVE → LIMITÉE → SUPPRIMÉE

### Règles de suppression

* Signalements négatifs multiples
* Suppression automatique au-delà d’un seuil

---

## 9. Données principales

### Entités clés

* Utilisateur
* Alerte
* Signalement
* Position géographique

### Données géographiques

* Latitude / Longitude
* Rayon de diffusion
* Calcul spatial via PostGIS

---

## 10. Notifications

### Type

* Push notifications temps réel

### Contenu

* Type d’alerte
* Message clair
* Gravité
* Position

---

## 11. Contraintes techniques

* Connexion réseau variable
* Priorité mobile
* Sécurité et confidentialité
* Scalabilité progressive

---

## 12. Évolutivité prévue

* Vote communautaire
* Score de fiabilité utilisateur
* Notifications SMS
* Tableau de bord autorités avancé
* Intelligence artificielle

---

## 13. Indicateurs de performance

* Temps de notification < 5 secondes
* Disponibilité API > 99%
* Taux de fausses alertes réduit

---

📌 **Cette fiche technique sert de référence pour le développement, la maintenance et l’évolution du système.**
