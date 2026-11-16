package com.aether.character.infrastructure.persistence;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface SpringDataCharacterRepository
    extends JpaRepository<CharacterJpaEntity, UUID> {
}
