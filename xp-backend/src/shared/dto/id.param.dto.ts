import { Type } from 'class-transformer';
import { IsInt } from 'class-validator';

export class NumericIdDTO {
  @IsInt()
  @Type(() => Number)
  id: number;
}
