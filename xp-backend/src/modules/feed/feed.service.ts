import { HttpException, Injectable } from '@nestjs/common';
import { ExperimentRepository } from '../experiment/repository/experiment.repository';
import { ExperimentViewRepository } from '../experiment/repository/experiment-view.repository';
import { PaginatedResponse } from 'src/shared/paginated.repository';
import { Experiment } from '../experiment/entities/experiment.entity';

class ExceededRandomExperimentsException extends HttpException {
  constructor() {
    super('EXCEEDED_RANDOM_EXPERIMENTS', 429);
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

  async getRandomExperiments(
    forUserId: number,
    limit = VIEW_LIMIT_PER_WEEK,
  ): Promise<PaginatedResponse<Experiment>> {
    const seenLastWeek = await this.experimentViewRepository.seenLastWeek(
      forUserId,
    );
    if (seenLastWeek >= VIEW_LIMIT_PER_WEEK) {
      throw new ExceededRandomExperimentsException();
    }

    const maxAvailable = VIEW_LIMIT_PER_WEEK - seenLastWeek;

    const experiments =
      await this.experimentRepository.getRandomUnseenExperiments(
        forUserId,
        Math.min(maxAvailable, limit),
      );

    return { items: experiments, next_key: null };
  }

  async getExperimentsFromFollowee(userId: number, limit = 10) {
    return this.experimentRepository.getLatestExperimentsFromFollowee(
      userId,
      limit,
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

  async markManyExperimentsAsSeen(userId: number, experimentsIds: number[]) {
    await this.experimentViewRepository.markManyExperimentsAsViewed(
      userId,
      experimentsIds,
    );
  }
}
