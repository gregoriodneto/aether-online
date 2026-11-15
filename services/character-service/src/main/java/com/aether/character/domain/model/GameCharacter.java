package com.aether.character.domain.model;

import java.util.UUID;

public class GameCharacter {
    private final UUID id;
    private final UUID serverId;
    private final String name;
    private final CharacterClass characterClass;
    private int level;

    public GameCharacter(
            UUID id,
            UUID serverId,
            String name,
            CharacterClass characterClass
    ) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException(
                    "Character name cannot be empty"
            );
        }

        if (name.length() < 3 || name.length() > 50) {
            throw new IllegalArgumentException(
                    "Character name must have 3 to 50 characters"
            );
        }

        if (id == null || serverId == null || characterClass == null) {
            throw new IllegalArgumentException(
                    "Required character fields cannot be null"
            );
        }

        this.id = id;
        this.serverId = serverId;
        this.name = name;
        this.characterClass = characterClass;
        this.level = 1;
    }

    public UUID getId() {
        return id;
    }

    public UUID getServerId() {
        return serverId;
    }

    public String getName() {
        return name;
    }

    public CharacterClass getCharacterClass() {
        return characterClass;
    }

    public int getLevel() {
        return level;
    }

    public void levelUp(int levels) {
        if (levels <= 0) {
            throw new IllegalArgumentException(
                    "Levels must be positive"
            );
        }

        if (levels > 99 - this.level) {
            throw new IllegalArgumentException(
                    "Maximum level is 99"
            );
        }

        this.level += levels;
    }
}
