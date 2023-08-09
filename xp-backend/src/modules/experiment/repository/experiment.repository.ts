import { Injectable } from '@nestjs/common';
import { DataSource, Repository } from 'typeorm';
import { Experiment } from '../entities/experiment.entity';

@Injectable()
export class ExperimentRepository extends Repository<Experiment> {
  constructor(dataSource: DataSource) {
    super(Experiment, dataSource.createEntityManager());
  }
}
