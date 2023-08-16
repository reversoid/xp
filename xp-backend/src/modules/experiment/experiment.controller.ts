import {
  Body,
  Controller,
  Delete,
  Get,
  Patch,
  Put,
  Request,
  UseGuards,
} from '@nestjs/common';
import { ExperimentService } from './experiment.service';
import { FinishExperimentDTO } from './dto/finish-experiment.dto';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { StartExperimentDTO } from './dto/start-experiment.dto';

@Controller('experiment')
export class ExperimentController {
  constructor(private experimentService: ExperimentService) {}

  @Get()
  @UseGuards(AuthGuard)
  async getCurrentExperiment(@Request() { user }: { user: User }) {
    return this.experimentService.getCurrentExperiment(user.id);
  }

  @Put()
  @UseGuards(AuthGuard)
  async runExperiment(
    @Request() { user }: { user: User },
    @Body() { observations_ids }: StartExperimentDTO,
  ) {
    return this.experimentService.runExperiment(user.id, observations_ids);
  }

  @Patch()
  @UseGuards(AuthGuard)
  async finishExperiment(
    @Request() { user }: { user: User },
    @Body() dto: FinishExperimentDTO,
  ) {
    return this.experimentService.finishExperiment(user.id, dto);
  }

  @Delete()
  @UseGuards(AuthGuard)
  async cancelExperiment(@Request() { user }: { user: User }) {
    return this.experimentService.cancelExperiment(user.id);
  }
}
