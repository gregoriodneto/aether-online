package com.aether.character.interfaces.rest;

import com.aether.character.application.service.CreateCharacterService;
import com.aether.character.domain.model.CharacterClass;
import com.aether.character.infrastructure.persistence.CharacterJpaEntity;
import com.aether.character.infrastructure.persistence.SpringDataCharacterRepository;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/characters")
public class CharacterController {

    private final CreateCharacterService service;
    private final SpringDataCharacterRepository repository;

    public CharacterController(
            CreateCharacterService service,
            SpringDataCharacterRepository repository
    ) {
        this.service = service;
        this.repository = repository;
    }

    public record CreateRequest(
            @NotNull UUID serverId,
            @NotBlank @Size(min = 3, max = 50) String name,
            @NotNull CharacterClass characterClass
    ) {}

    @PostMapping
    public ResponseEntity<Map<String, UUID>> create(
            @Valid @RequestBody CreateRequest request
    ) {
        UUID id = service.execute(
                request.serverId(),
                request.name(),
                request.characterClass()
        );

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(Map.of("id", id));
    }

    @GetMapping("/{id}")
    public ResponseEntity<CharacterJpaEntity> findById(
        @PathVariable UUID id
    ) {
        return repository.findById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @GetMapping
    public List<CharacterJpaEntity> findAll() {
        return repository.findAll();
    }
}
