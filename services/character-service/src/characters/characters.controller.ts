import { Body, Controller, Post } from '@nestjs/common';
import { CharactersService } from './characters.service';
import { CreateCharacterDto } from './dto/create-character.dto';

@Controller('characters')
export class CharactersController {
    constructor(
        private readonly characterService: CharactersService
    ) { }

    @Post()
    create(@Body() dto: CreateCharacterDto) {
        return this.characterService.create(dto);
    }
}
