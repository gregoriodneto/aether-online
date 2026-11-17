import { Injectable } from '@nestjs/common';
import { CreateCharacterDto } from './dto/create-character.dto';
import { GameCharacter } from './domain/game-character';

@Injectable()
export class CharactersService {
    create(dto: CreateCharacterDto) {
        const character = new GameCharacter(
            dto.serverId,
            dto.name,
            dto.characterClass
        );

        return {
            id: character.id,
            serverId: character.serverId,
            name: character.name,
            characterClass: character.characterClass,
            level: character.getLevel(),
        };
    }
}
