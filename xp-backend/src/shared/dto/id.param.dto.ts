import { Type } from 'class-transformer';
import { IsInt } from 'class-validator';

export class NumericIdParamDTO {
  @IsInt()
  @Type(() => Number)
  id: number;
}
