import { Injectable } from '@nestjs/common';
import { ObservationRepository } from '../observation/repositories/observation.repository';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';

@Injectable()
export class ProfileService {
  constructor(
    private readonly observationRepository: ObservationRepository,
    private readonly experimentRepository: ExperimentRepository,
  ) {}

  async getUserObservations(userId: number) {
    return this.observationRepository.getUserObservations(userId);
  }

  async getUserExperiments(userId: number) {
    return this.experimentRepository.getUserExperiments(userId);
  }
}
