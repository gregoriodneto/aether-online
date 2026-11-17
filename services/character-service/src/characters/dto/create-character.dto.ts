import {
  IsEnum,
  IsNotEmpty,
  IsString,
  IsUUID,
  Length,
} from 'class-validator';

export enum CharacterClass {
    WARRIOR = 'WARRIOR',
    MAGE = 'MAGE',
    ARCHER = 'ARCHER',
}

export class CreateCharacterDto {
    @IsUUID()
    serverId!: string;

    @IsString()
    @IsNotEmpty()
    @Length(3, 50)
    name!: string;

    @IsEnum(CharacterClass)
    characterClass!: CharacterClass;
}