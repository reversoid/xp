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
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';

@Controller('experiment')
export class ExperimentController {
  constructor(private experimentService: ExperimentService) {}

  @Put()
  @UseGuards(AuthGuard)
  async runExperiment(@Request() { user }: { user: User }) {
    return this.experimentService.runExperiment(user.id);
  }

  @Patch()
  @UseGuards(AuthGuard)
  async finishExperiment(
    @Request() { user }: { user: any },
    @Body() dto: FinishExperimentDTO,
  ) {
    return this.experimentService.finishExperiment(user.id, dto);
  }

  @Delete()
  @UseGuards() // TODO use some auth guard
  async cancelExperiment(@Request() { user }: { user: any }) {
    return this.experimentService.cancelExperiment(user.id);
  }
}
