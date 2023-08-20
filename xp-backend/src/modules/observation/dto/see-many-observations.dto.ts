import { IsInt } from 'class-validator';

export class SeeManyObservationsDTO {
  @IsInt({ each: true })
  observations_ids: number[];
}
