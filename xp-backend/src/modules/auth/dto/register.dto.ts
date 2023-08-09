import { IsInt, IsOptional, IsString, MaxLength } from 'class-validator';

export class RegisterDTO {
  @IsInt()
  @IsOptional()
  tg_user_id?: number;

  @IsString()
  @MaxLength(32)
  username: string;

  @IsString()
  password: string;
}
