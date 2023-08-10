import { Type } from 'class-transformer';
import { IsInt } from 'class-validator';

export class IsRegisteredQueryDTO {
  @IsInt()
  @Type(() => Number)
  tg_user_id: number;
}
