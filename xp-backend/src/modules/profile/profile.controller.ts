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

@Controller('profile')
export class ProfileController {
  constructor(private profileService: ProfileService) {}

  @Get('observations')
  @UseGuards(AuthGuard)
  async getMyObservations(
    @Request() { user }: { user: User },
    @Query() { limit = 10, lower_bound }: PaginationQueryDTO,
  ): Promise<PaginatedResponse<Observation>> {
    return this.profileService.getUserObservations(user.id, limit, lower_bound);
  }

  @Get('experiments')
  @UseGuards(AuthGuard)
  async getMyExperiments(
    @Request() { user }: { user: User },
    @Query() { limit = 10, lower_bound }: PaginationQueryDTO,
  ) {
    return this.profileService.getUserExperiments(user.id, limit, lower_bound);
  }

  @Get('followees')
  @UseGuards(AuthGuard)
  async getMyFollowees(
    @Request() { user }: { user: User },
    @Query() { limit, lower_bound }: PaginationQueryDTO,
  ) {
    return this.profileService.getUserFollowees(user.id, limit, lower_bound);
  }

  @Put(':username/followers')
  @UseGuards(AuthGuard)
  async followUser(
    @Request() { user }: { user: User },
    @Param() { username }: ProfileUsernameParamDTO,
  ) {
    return this.profileService.followUser(user.id, username);
  }

  @Delete(':username/followers')
  @UseGuards(AuthGuard)
  async unFollowUser(
    @Request() { user }: { user: User },
    @Param() { username }: ProfileUsernameParamDTO,
  ) {
    return this.profileService.unFollowUser(user.id, username);
  }
}
