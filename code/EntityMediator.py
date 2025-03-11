import pygame

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:
    @staticmethod
    # method private
    def __verify_collision_window(ent: Entity):
        # pass
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, Player):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            has_collided = pygame.Rect.colliderect(ent1.rect, ent2.rect)
            if has_collided:
                # Check if the entities have already collided
                if ent2 not in ent1.collided_with:
                    # Apply damage
                    if isinstance(ent1, Player):
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name
                    elif isinstance(ent2, Player):
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name

                    # Mark the entities as having collided
                    ent1.collided_with.add(ent2)
                    ent2.collided_with.add(ent1)

                    print(f"Collision: {ent1.name} and {ent2.name}")
                    print(f"{ent1.name} health: {ent1.health}, {ent2.name} health: {ent2.health}")
            else:
                # Reset the collision tracking if the entities are no longer colliding
                if ent2 in ent1.collided_with:
                    ent1.collided_with.remove(ent2)
                if ent1 in ent2.collided_with:
                    ent2.collided_with.remove(ent1)


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod
    def __give_score(enemy:Enemy, entity_list: list[Entity]):
        pass
        # if enemy.last_dmg == 'Player1Shot':
        #     for ent in entity_list:
        #         if ent.name == 'Player1':
        #             ent.score += enemy.score
        # elif enemy.last_dmg == 'Player2Shot':
        #     for ent in entity_list:
        #         if ent.name == 'Player2':
        #             ent.score += enemy.score