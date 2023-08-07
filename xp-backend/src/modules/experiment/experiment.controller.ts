import {
  Body,
  Controller,
  Delete,
  Patch,
  Put,
  Request,
  UseGuards,
} from '@nestjs/common';
import { ExperimentService } from './experiment.service';
import { FinishExperimentDTO } from './dto/finish-experiment.dto';

@Controller('experiment')
export class ExperimentController {
  constructor(private experimentService: ExperimentService) {}

  @Put()
  @UseGuards() // TODO use some auth guard
  async runExperiment(@Request() { user }: { user: any }) {
    return this.experimentService.runExperiment(user.id);
  }

  @Patch()
  @UseGuards() // TODO use some auth guard
  async finishExperiment(
    @Body() dto: FinishExperimentDTO,
    @Request() { user }: { user: any },
  ) {
    return this.experimentService.finishExperiment(user.id, dto);
  }

  @Delete()
  @UseGuards() // TODO use some auth guard
  async cancelExperiment(@Request() { user }: { user: any }) {
    return this.experimentService.cancelExperiment(user.id);
  }
}
