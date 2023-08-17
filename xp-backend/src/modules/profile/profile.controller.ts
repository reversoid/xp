import {
  Controller,
  Delete,
  Get,
  Param,
  Put,
  Query,
  Request,
  UseGuards,
} from '@nestjs/common';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { ProfileService } from './profile.service';
import { PaginationQueryDTO } from 'src/shared/dto/paginated-query.dto';
import { PaginatedResponse } from 'src/shared/paginated.repository';
import { Observation } from '../observation/entities/observation.entity';
import { ProfileUsernameParamDTO } from './dto/profile-username.param.dto copy';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { SwaggerPaginatedResponse } from 'src/shared/swagger/responses/Paginated.response';
import { ObservationResponse } from 'src/shared/swagger/responses/ObservationResponse';
import { ExperimentResponse } from 'src/shared/swagger/responses/Experiment.response';
import { UserResponse } from 'src/shared/swagger/responses/User.response';
import { ExperimentPaginatedResponse } from 'src/shared/swagger/responses/ExperimentPaginated.response';
import { ObservationPaginatedResponse } from 'src/shared/swagger/responses/ObservationPaginated.response';
import { UserPaginatedResponse } from 'src/shared/swagger/responses/UserPaginatedResponse';

@ApiTags('Profile')
@Controller('profile')
export class ProfileController {
  constructor(private profileService: ProfileService) {}

  @ApiOperation({ description: 'Get my observations' })
  @ApiResponse({
    description: 'My observations',
    type: ObservationPaginatedResponse,
  })
  @Get('observations')
  @UseGuards(AuthGuard)
  async getMyObservations(
    @Request() { user }: { user: User },
    @Query() { limit = 10, lower_bound }: PaginationQueryDTO,
  ): Promise<PaginatedResponse<Observation>> {
    return this.profileService.getUserObservations(user.id, limit, lower_bound);
  }

  @ApiOperation({ description: 'Get my experiments' })
  @ApiResponse({
    description: 'My Experiments',
    type: ExperimentPaginatedResponse,
  })
  @Get('experiments')
  @UseGuards(AuthGuard)
  async getMyExperiments(
    @Request() { user }: { user: User },
    @Query() { limit = 10, lower_bound }: PaginationQueryDTO,
  ) {
    return this.profileService.getUserExperiments(user.id, limit, lower_bound);
  }

  @ApiOperation({ description: 'Get my followees' })
  @ApiResponse({
    description: 'My followees',
    type: UserPaginatedResponse,
  })
  @Get('followees')
  @UseGuards(AuthGuard)
  async getMyFollowees(
    @Request() { user }: { user: User },
    @Query() { limit, lower_bound }: PaginationQueryDTO,
  ) {
    return this.profileService.getUserFollowees(user.id, limit, lower_bound);
  }

  @ApiOperation({ description: 'Follow a user' })
  @Put(':username/followers')
  @UseGuards(AuthGuard)
  async followUser(
    @Request() { user }: { user: User },
    @Param() { username }: ProfileUsernameParamDTO,
  ) {
    await this.profileService.followUser(user.id, username);
  }

  @ApiOperation({ description: 'Unfollow a user' })
  @Delete(':username/followers')
  @UseGuards(AuthGuard)
  async unFollowUser(
    @Request() { user }: { user: User },
    @Param() { username }: ProfileUsernameParamDTO,
  ) {
    return this.profileService.unFollowUser(user.id, username);
  }
}
