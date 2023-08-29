import { IsInt } from 'class-validator';

export class StartExperimentDTO {
  @IsInt({ each: true })
  observations_ids: number[];
}
