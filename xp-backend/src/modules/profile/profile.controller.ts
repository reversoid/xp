import { Controller, Get, Request, UseGuards } from '@nestjs/common';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { ProfileService } from './profile.service';

@Controller('profile')
export class ProfileController {
  constructor(private profileService: ProfileService) {}

  @Get('observations')
  @UseGuards(AuthGuard)
  async getMyObservations(@Request() { user }: { user: User }) {
    return this.profileService.getUserObservations(user.id);
  }

  @Get('experiments')
  @UseGuards(AuthGuard)
  async getMyExperiments(@Request() { user }: { user: User }) {
    return this.profileService.getUserExperiments(user.id);
  }
}
