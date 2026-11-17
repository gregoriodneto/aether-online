var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { IsEnum, IsNotEmpty, IsString, IsUUID, Length, } from 'class-validator';
export var CharacterClass;
(function (CharacterClass) {
    CharacterClass["WARRIOR"] = "WARRIOR";
    CharacterClass["MAGE"] = "MAGE";
    CharacterClass["ARCHER"] = "ARCHER";
})(CharacterClass || (CharacterClass = {}));
export class CreateCharacterDto {
    serverId;
    name;
    characterClass;
}
__decorate([
    IsUUID(),
    __metadata("design:type", String)
], CreateCharacterDto.prototype, "serverId", void 0);
__decorate([
    IsString(),
    IsNotEmpty(),
    Length(3, 50),
    __metadata("design:type", String)
], CreateCharacterDto.prototype, "name", void 0);
__decorate([
    IsEnum(CharacterClass),
    __metadata("design:type", String)
], CreateCharacterDto.prototype, "characterClass", void 0);
