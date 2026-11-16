package com.aether.character.infrastructure.persistence;

import jakarta.persistence.*;

import java.time.OffsetDateTime;
import java.util.UUID;

@Entity
@Table(name = "characters")
public class CharacterJpaEntity {
    @Id
    private UUID id;

    @Column(name = "server_id", nullable = false)
    private UUID serverId;

    @Column(nullable = false)
    private String name;

    @Column(name = "character_class", nullable = false)
    private String characterClass;

    @Column(nullable = false)
    private int level;

    @Version
    private Long version;

    @Column(name = "created_at", insertable = false, updatable = false)
    private OffsetDateTime createdAt;

    protected CharacterJpaEntity() {}

    public CharacterJpaEntity(
            UUID id,
            UUID serverId,
            String name,
            String characterClass,
            int level
    ) {
        this.id = id;
        this.serverId = serverId;
        this.name = name;
        this.characterClass = characterClass;
        this.level = level;
    }

    public UUID getId() { return id; }
    public UUID getServerId() { return serverId; }
    public String getName() { return name; }
    public String getCharacterClass() { return characterClass; }
    public int getLevel() { return level; }
}
