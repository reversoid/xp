import { HttpException, Injectable } from '@nestjs/common';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { ExperimentViewRepository } from '../experiment/repository/experiment-view.repository';
import { ExperimentView } from '../experiment/entities/experiment-view.entity';
import { DeepPartial } from 'typeorm';

class ExperimentsViewsExceededException extends HttpException {
  constructor() {
    super('VIEWS_EXCEEDED', 423);
  }
}

/** Amount of experiments user is able to see a week */
export const VIEW_LIMIT_PER_WEEK = 10;

@Injectable()
export class FeedService {
  constructor(
    private readonly experimentRepository: ExperimentRepository,
    private readonly experimentViewRepository: ExperimentViewRepository,
  ) {}

  async getExperiments(forUserId: number) {
    const seenLastWeek = await this.experimentViewRepository.seenLastWeek(
      forUserId,
    );
    if (seenLastWeek >= VIEW_LIMIT_PER_WEEK) {
      throw new ExperimentsViewsExceededException();
    }

    return this.experimentRepository.getRandomUnseenExperiments(
      forUserId,
      VIEW_LIMIT_PER_WEEK - seenLastWeek,
    );
  }

  async markExperimentAsSeen(userId: number, experimentId: number) {
    const isSeen = await this.experimentViewRepository.isExperimentViewed(
      userId,
      experimentId,
    );
    if (isSeen) {
      return;
    }
    await this.experimentViewRepository.markExperimentAsViewed(
      userId,
      experimentId,
    );
  }

  async markManyExperimentsAsSeen(userId: number, experiments_ids: number[]) {
    await this.experimentViewRepository.save(
      experiments_ids.map<DeepPartial<ExperimentView>>((id) => ({
        user: { id: userId },
        experiment: { id },
      })),
    );
  }
}
