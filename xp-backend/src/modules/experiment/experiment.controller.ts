import {
  Controller,
  NotImplementedException,
  Patch,
  Post,
  UseGuards,
} from '@nestjs/common';

@Controller('experiment')
export class ExperimentController {
  @Post()
  @UseGuards() // TODO use some auth guard
  async runExperiment() {
    throw new NotImplementedException();
  }

  @Patch()
  @UseGuards() // TODO use some auth guard
  async finishExperiment() {
    throw new NotImplementedException();
  }
}
