import { Type } from 'class-transformer';
import { IsBoolean, IsOptional } from 'class-validator';

export class AuthQueryDTO {
  @IsOptional()
  @IsBoolean()
  @Type(() => Boolean)
  suppress_tokens?: boolean;
}
