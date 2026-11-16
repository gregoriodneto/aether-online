package com.aether.character.application.service;

import com.aether.character.domain.model.CharacterClass;
import com.aether.character.domain.model.GameCharacter;
import com.aether.character.infrastructure.persistence.CharacterJpaEntity;
import com.aether.character.infrastructure.persistence.SpringDataCharacterRepository;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class CreateCharacterService {

    private final SpringDataCharacterRepository repository;

    public CreateCharacterService(
            SpringDataCharacterRepository repository
    ) {
        this.repository = repository;
    }

    @Transactional
    public UUID execute(
            UUID serverId,
            String name,
            CharacterClass characterClass
    ) {
        GameCharacter character = new GameCharacter(
                UUID.randomUUID(),
                serverId,
                name,
                characterClass
        );

        CharacterJpaEntity entity = new CharacterJpaEntity(
                character.getId(),
                character.getServerId(),
                character.getName(),
                character.getCharacterClass().name(),
                character.getLevel()
        );

        repository.saveAndFlush(entity);

        return character.getId();
    }
}
