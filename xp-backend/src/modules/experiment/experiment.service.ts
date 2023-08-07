import { Injectable, NotImplementedException } from '@nestjs/common';
import { FinishExperimentDTO } from './dto/finish-experiment.dto';

@Injectable()
export class ExperimentService {
  async runExperiment(userId: number) {
    throw new NotImplementedException({ userId });
  }

  async finishExperiment(userId: number, dto: FinishExperimentDTO) {
    throw new NotImplementedException({ userId, dto });
  }

  async cancelExperiment(userId: number) {
    throw new NotImplementedException({ userId });
  }
}
