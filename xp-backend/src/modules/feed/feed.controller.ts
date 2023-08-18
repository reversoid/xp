import {
  Body,
  Controller,
  Get,
  Param,
  Put,
  Query,
  Request,
  UseGuards,
} from '@nestjs/common';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { FeedService } from './feed.service';
import { NumericIdParamDTO } from 'src/shared/dto/id.param.dto';
import { SeeManyExperimentsDTO } from './dto/see-many-experiments.dto';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { ExperimentResponse } from 'src/shared/swagger/responses/Experiment.response';
import { LimitQueryDTO } from 'src/shared/dto/limit.query.dto';

@ApiTags('Feed')
@Controller('feed')
export class FeedController {
  constructor(private readonly feedService: FeedService) {}

  @ApiOperation({ description: 'Get random experiments' })
  @ApiResponse({
    type: ExperimentResponse,
    isArray: true,
    description: 'Random experiments from all users',
  })
  @Get('experiments/random')
  @UseGuards(AuthGuard)
  async getRandomExperiments(
    @Request() { user }: { user: User },
    @Query() { limit }: LimitQueryDTO,
  ) {
    return this.feedService.getRandomExperiments(user.id, limit);
  }

  @ApiOperation({ description: 'Get latest experiments from your followee' })
  @ApiResponse({
    type: ExperimentResponse,
    isArray: true,
    description: 'Latest experiments',
  })
  @Get('experiments/followee')
  @UseGuards(AuthGuard)
  async getExperimentsFromFollowee(
    @Request() { user }: { user: User },
    @Query() { limit }: LimitQueryDTO,
  ) {
    return this.feedService.getExperimentsFromFollowee(user.id, limit);
  }

  @ApiOperation({ description: 'Mark experiment as seen' })
  @Put('experiment/:id/views')
  @UseGuards(AuthGuard)
  async markExperimentAsSeen(
    @Request() { user }: { user: User },
    @Param() { id }: NumericIdParamDTO,
  ) {
    return this.feedService.markExperimentAsSeen(user.id, id);
  }

  @ApiOperation({ description: 'Mark many experiments as seen' })
  @Put('experiment/views')
  @UseGuards(AuthGuard)
  async markManyExperimentsAsSeen(
    @Request() { user }: { user: User },
    @Body() { experiments_ids }: SeeManyExperimentsDTO,
  ) {
    return this.feedService.markManyExperimentsAsSeen(user.id, experiments_ids);
  }
}
