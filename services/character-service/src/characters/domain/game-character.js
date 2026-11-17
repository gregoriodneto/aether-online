import { randomUUID } from "node:crypto";
export class GameCharacter {
    id;
    serverId;
    name;
    characterClass;
    level = 1;
    constructor(serverId, name, characterClass) {
        this.id = randomUUID();
        this.serverId = serverId;
        this.name = name;
        this.characterClass = characterClass;
    }
    levelUp(levels) {
        if (!Number.isSafeInteger(levels) || levels <= 0) {
            throw new Error("Levels must be positive integers");
        }
        if (levels > 99 - this.level) {
            throw new Error("Maximum level is 99");
        }
    }
    getLevel() {
        return this.level;
    }
}
