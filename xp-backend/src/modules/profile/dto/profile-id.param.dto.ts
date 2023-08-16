import { Type } from 'class-transformer';
import { IsInt } from 'class-validator';

export class ProfileIdParamDTO {
  @IsInt()
  @Type(() => Number)
  id: number;
}
