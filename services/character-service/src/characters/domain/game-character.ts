import { randomUUID } from "node:crypto";
import { CharacterClass } from "../dto/create-character.dto";

export class GameCharacter {
    readonly id: string;
    readonly serverId: string;
    readonly name: string;
    readonly characterClass: CharacterClass;
    private level = 1;


    constructor(
        serverId: string,
        name: string,
        characterClass: CharacterClass
    ) {
        this.id = randomUUID();
        this.serverId = serverId;
        this.name = name;
        this.characterClass = characterClass;
    }

    levelUp(levels: number): void {
        if (!Number.isSafeInteger(levels) || levels <= 0) {
            throw new Error("Levels must be positive integers");
        }

        if (levels > 99 - this.level) {
            throw new Error("Maximum level is 99");
        }
    }

    getLevel(): number {
        return this.level;
    }
}