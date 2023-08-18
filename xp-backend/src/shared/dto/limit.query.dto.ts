import { IsInt, IsOptional } from 'class-validator';
import { Type } from 'class-transformer';

export class LimitQueryDTO {
  @IsOptional()
  @IsInt()
  @Type(() => Number)
  limit?: number;
}
