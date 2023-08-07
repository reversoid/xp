import { Type } from 'class-transformer';
import { IsInt, IsOptional } from 'class-validator';

export class GetRandomObservations {
  @IsOptional()
  @IsInt()
  @Type(() => Number)
  amount?: number;
}
