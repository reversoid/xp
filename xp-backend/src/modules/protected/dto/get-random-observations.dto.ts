import { Type } from 'class-transformer';
import { IsInt } from 'class-validator';

export class GetRandomObservations {
  @IsInt()
  @Type(() => Number)
  userId: number;
}
