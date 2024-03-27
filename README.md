# Strategy Pattern: AI-Behaviour
**This is a small project to practice the Strategy Pattern.**
It was made with the idea of a simple ASCII RPG game, where enemies could switch behaviour depending on circumstances.
In a full-scale project this could have been managed by a "Game Master" algorithm who would control groups of/separate entities changing their behaviour on the go or it could have been changed by the entity itself based on its own state or/and state of its environment. There are many options for in-game AI control.
This project is not fully fleshed-out as it was used just for the Strategy Pattern itself. I did put some more time and effort into Pathfinding as I find it fun and challenging.
Inventory and ItemsCore are made as prototype cases only to be used for testing of HasBehaviour code. Initially, I wanted to also include spellcasting, but this would further side-track this project, so in the end these are technically unused.

## Content:
**IsEntity** - Is the main file for code related to entities. In a bigger project this could be developed in to few different entity categories for different objects with Factory Pattern to decide which one to create if the game would use procedural generation of entities.

**HasBehaviour** - Defines different classes of behaviour. Only three of them are implemented: IsAggressive, IsDefensive and IsCowardly. All behaviours decide what the entity will do when it comes to moving around and attacking. E.g: Aggressive will move towards the target and choose the most damaging weapon. These can be mixed and matched with e.g. using move pattern of move_towards() but instead of picking the most damaging weapon, the entity could use the best shield and best one-handed weapon. 

**Pathfinders** - Deals with pathfinding, checking up positions on the map and calculating distances.
Other files do not require much attention.
