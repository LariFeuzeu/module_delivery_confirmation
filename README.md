# module_delivery_confirmation_Odoo.11

## Description 📦

Ce module permet de confirmer la sortie physique des marchandises du stock dans Odoo11. Cela facilite la gestion des inventaires et le suivi des stocks. 

Il inclut les fonctionnalités suivantes :
- **Confirmation de la sortie physique des marchandises** : permet de suivre la sortie physique des produits.
- **Mise à jour de l'état physique du bon de commande** : l'état du bon de commande peut être défini comme :
  - **Livraison en attente**
  - **Livraison partielle**
  - **Livraison effectuée**
  
- **Réflexion des changements d'état sur la facture** : l'état de la livraison physique du bon de commande est également reflété sur la facture associée.

- **Filtres pour la gestion des commandes et factures** : 
  - Vous pouvez filtrer les bons de commande selon leur état de livraison (en attente, partielle, terminée).
  - Les factures peuvent également être filtrées en fonction de leur état de livraison physique (en attente, partielle, terminée).

## Fonctionnalités 🚀

### 1. **Confirmation de la Sortie Physique**
Lorsqu'une sortie de stock est confirmée, l'état physique des marchandises est mis à jour et l'état du bon de commande est modifié en conséquence (Livraison en attente, Livraison partielle ou Livraison effectuée).

### 2. **Gestion de l'État de Livraison sur le Bon de Commande**
Le module ajoute un champ sur le bon de commande pour refléter l'état de la livraison physique :
- **Livraison en attente** : L'état par défaut lorsque la livraison n'a pas encore été confirmée.
- **Livraison partielle** : Si une partie des produits a été livrée, l'état est mis à jour en "Livraison partielle".
- **Livraison effectuée** : Si la livraison a été complètement effectuée.

### 3. **Mise à Jour de l'État sur la Facture**
Lorsque l'état de la livraison physique est modifié sur le bon de commande, l'état est également mis à jour sur la facture associée pour un suivi cohérent.

### 4. **Filtres de Recherche**
Les utilisateurs peuvent facilement filtrer les bons de commande et les factures en fonction de leur état de livraison physique :
- **Filtrer les bons de commande par état** : En attente, Partielle, Terminée.
- **Filtrer les factures par état de livraison** : En attente, Partielle, Terminée.

## Installation 🛠

1. Téléchargez ou clonez ce module dans votre répertoire Odoo.
2. Placez-le dans le dossier `addons` de votre instance Odoo.
3. Activez le mode développeur dans Odoo.
4. Allez dans "Applications" et mettez à jour la liste des applications.
5. Recherchez "module_delivery_confirmation" et installez-le.

## Utilisation 📊

### Bon de Commande
- Après avoir créé un bon de commande, l'utilisateur peut confirmer la sortie des marchandises en stock via un bouton "Livraison effectuée".
- L'état de la livraison sur le bon de commande est mis à jour en fonction de la confirmation physique.

### Factures
- L'état de livraison physique du bon de commande est automatiquement répercuté sur la facture associée, offrant ainsi un suivi précis et cohérent des livraisons.

### Filtres
- Vous pouvez filtrer les bons de commande et les factures par état de livraison via les filtres dans les vues de recherche.

## Contribution 🤝

Les contributions sont les bienvenues. Pour contribuer à ce projet, veuillez suivre les étapes suivantes :
1. Fork ce dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature-nom-fonctionnalité`).
3. Commitez vos changements (`git commit -am 'Ajout de fonctionnalité'`).
4. Poussez la branche (`git push origin feature-nom-fonctionnalité`).
5. Créez une Pull Request.

