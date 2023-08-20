import { IsString, MaxLength } from 'class-validator';

export class ProfileUsernameDTO {
  @IsString()
  @MaxLength(32)
  username: string;
}
