import { Injectable } from '@nestjs/common';
import { ObservationRepository } from '../observation/repositories/observation.repository';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { DateTime } from 'luxon';

@Injectable()
export class ProfileService {
  constructor(
    private readonly observationRepository: ObservationRepository,
    private readonly experimentRepository: ExperimentRepository,
  ) {}

  async getUserObservations(
    userId: number,
    limit: number,
    lowerBound?: DateTime,
  ) {
    return this.observationRepository.getUserObservations(
      userId,
      limit,
      lowerBound,
    );
  }

  async getUserExperiments(
    userId: number,
    limit: number,
    lower_bound: DateTime,
  ) {
    return this.experimentRepository.getUserCompletedExperiments(
      userId,
      limit,
      lower_bound,
    );
  }
}
