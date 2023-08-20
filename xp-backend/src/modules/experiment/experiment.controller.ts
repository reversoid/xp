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
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { ExperimentResponse } from '../../shared/swagger/responses/Experiment.response';

@ApiTags('Experiment')
@Controller('experiments')
export class ExperimentController {
  constructor(private experimentService: ExperimentService) {}

  @ApiOperation({ description: 'Get current experiment' })
  @ApiResponse({ description: 'Current experiment', type: ExperimentResponse })
  @Get()
  @UseGuards(AuthGuard)
  async getCurrentExperiment(@Request() { user }: { user: User }) {
    return this.experimentService.getCurrentExperiment(user.id);
  }

  @ApiOperation({ description: 'Run experiment' })
  @ApiResponse({ description: 'New experiment', type: ExperimentResponse })
  @Put()
  @UseGuards(AuthGuard)
  async runExperiment(
    @Request() { user }: { user: User },
    @Body() { observations_ids }: StartExperimentDTO,
  ) {
    return this.experimentService.runExperiment(user.id, observations_ids);
  }

  @ApiOperation({ description: 'Finish experiment' })
  @ApiResponse({
    description: 'Completed experiment',
    type: ExperimentResponse,
  })
  @Patch()
  @UseGuards(AuthGuard)
  async finishExperiment(
    @Request() { user }: { user: User },
    @Body() dto: FinishExperimentDTO,
  ) {
    return this.experimentService.finishExperiment(user.id, dto);
  }

  @ApiOperation({ description: 'Cancel experiment' })
  @Delete()
  @UseGuards(AuthGuard)
  async cancelExperiment(@Request() { user }: { user: User }) {
    await this.experimentService.cancelExperiment(user.id);
  }
}
