import { IsInt } from 'class-validator';

export class SeeManyExperimentsDTO {
  @IsInt({ each: true })
  experiments_ids: number[];
}
