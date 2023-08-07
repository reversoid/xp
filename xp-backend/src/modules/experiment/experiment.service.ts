import { Injectable, NotImplementedException } from '@nestjs/common';

@Injectable()
export class ExperimentService {
  async runExperiment() {
    throw new NotImplementedException();
  }
}
